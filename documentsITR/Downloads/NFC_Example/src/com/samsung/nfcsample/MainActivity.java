package com.samsung.nfcsample;

import java.io.IOException;
import java.io.UnsupportedEncodingException;
import java.nio.charset.Charset;
import java.util.Arrays;
import java.util.Locale;

import android.annotation.TargetApi;
import android.app.Activity;
import android.app.PendingIntent;
import android.content.Intent;
import android.content.IntentFilter;
import android.content.IntentFilter.MalformedMimeTypeException;
import android.net.Uri;
import android.nfc.FormatException;
import android.nfc.NdefMessage;
import android.nfc.NdefRecord;
import android.nfc.NfcAdapter;
import android.nfc.Tag;
import android.nfc.TagLostException;
import android.nfc.tech.MifareClassic;
import android.nfc.tech.Ndef;
import android.nfc.tech.NdefFormatable;
import android.nfc.tech.NfcA;
import android.os.Build;
import android.os.Bundle;
import android.os.Handler;
import android.util.Log;
import android.view.MotionEvent;
import android.view.View;
import android.view.View.OnClickListener;
import android.widget.Button;
import android.widget.TextView;
import android.widget.Toast;

import com.samsung.nfcsample.util.SystemUiHider;

/**
 * An example full-screen activity that shows and hides the system UI (i.e.
 * status bar and navigation/system bar) with user interaction.
 * 
 * @see SystemUiHider
 */
public class MainActivity extends Activity {
	public static final String TAG = "NFC_Sample";
	public static final String DEFAULT_TEXT_MESSAGE = "Hello, NFC World!";
	public static final String DEFAULT_AAR_TEXT_MESSAGE = "AAR detected!";
	public static final String DEFAULT_URL = "http://developer.samsung.com";
	public static final String TEXT_PLAIN_MIME_TYPE = "text/plain";
	private static Tag mTag;
	private NdefRecord mNdefAARRecord = NdefRecord.createApplicationRecord("com.samsung.nfcsample");
	private NdefMessage mDefaultNdefURIMesssage = new NdefMessage(new NdefRecord[]{NdefRecord.createUri(DEFAULT_URL)});
	private NdefMessage mDefaultNdefTextMesssage = new NdefMessage(new NdefRecord[]{new NdefRecord(
			NdefRecord.TNF_MIME_MEDIA, TEXT_PLAIN_MIME_TYPE.getBytes(), new byte[0], DEFAULT_TEXT_MESSAGE.getBytes())});
	private NdefMessage mAARTextMesssage = new NdefMessage(new NdefRecord[]{
			new NdefRecord(NdefRecord.TNF_MIME_MEDIA, TEXT_PLAIN_MIME_TYPE.getBytes(), new byte[0],
					DEFAULT_AAR_TEXT_MESSAGE.getBytes()), mNdefAARRecord});
	private final Object syncObject = new Object();

	private enum WorkMode {
		MODE_READ, MODE_WRITE
	}
	WorkMode mMode = WorkMode.MODE_READ;
	// public AlertDialog mDialog;

	NfcAdapter mNfcAdapter;
	private PendingIntent mNfcPendingIntent;
	private IntentFilter[] mNdefFilters;

	/**
	 * Whether or not the system UI should be auto-hidden after
	 * {@link #AUTO_HIDE_DELAY_MILLIS} milliseconds.
	 */
	private static final boolean AUTO_HIDE = true;

	/**
	 * If {@link #AUTO_HIDE} is set, the number of milliseconds to wait after
	 * user interaction before hiding the system UI.
	 */
	private static final int AUTO_HIDE_DELAY_MILLIS = 3000;

	/**
	 * If set, will toggle the system UI visibility upon interaction. Otherwise,
	 * will show the system UI visibility upon interaction.
	 */
	private static final boolean TOGGLE_ON_CLICK = true;

	/**
	 * The flags to pass to {@link SystemUiHider#getInstance}.
	 */
	private static final int HIDER_FLAGS = SystemUiHider.FLAG_HIDE_NAVIGATION;

	/**
	 * The instance of the {@link SystemUiHider} for this activity.
	 */
	private SystemUiHider mSystemUiHider;

	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		Log.d(TAG, "MainActivity onCreate start");
		mNfcAdapter = NfcAdapter.getDefaultAdapter(this);

		setContentView(R.layout.activity_main);

		final View controlsView = findViewById(R.id.fullscreen_content_controls);
		final View contentView = findViewById(R.id.fullscreen_content);

		// Set up an instance of SystemUiHider to control the system UI for
		// this activity.
		mSystemUiHider = SystemUiHider.getInstance(this, contentView, HIDER_FLAGS);
		mSystemUiHider.setup();
		mSystemUiHider.setOnVisibilityChangeListener(new SystemUiHider.OnVisibilityChangeListener() {
			// Cached values.
			int mControlsHeight;
			int mShortAnimTime;

			@Override
			@TargetApi(Build.VERSION_CODES.HONEYCOMB_MR2)
			public void onVisibilityChange(boolean visible) {
				if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.HONEYCOMB_MR2) {
					// If the ViewPropertyAnimator API is available
					// (Honeycomb MR2 and later), use it to animate the
					// in-layout UI controls at the bottom of the
					// screen.
					if (mControlsHeight == 0) {
						mControlsHeight = controlsView.getHeight();
					}
					if (mShortAnimTime == 0) {
						mShortAnimTime = getResources().getInteger(android.R.integer.config_shortAnimTime);
					}
					controlsView.animate().translationY(visible ? 0 : mControlsHeight).setDuration(mShortAnimTime);
				} else {
					// If the ViewPropertyAnimator APIs aren't
					// available, simply show or hide the in-layout UI
					// controls.
					controlsView.setVisibility(visible ? View.VISIBLE : View.GONE);
				}

				if (visible && AUTO_HIDE) {
					// Schedule a hide().
					delayedHide(AUTO_HIDE_DELAY_MILLIS);
				}
			}
		});

		// Set up the user interaction to manually show or hide the system UI.
		contentView.setOnClickListener(new View.OnClickListener() {
			@Override
			public void onClick(View view) {
				if (TOGGLE_ON_CLICK) {
					mSystemUiHider.toggle();
				} else {
					mSystemUiHider.show();
				}
			}
		});

		// mDialog = new
		// AlertDialog.Builder(this).setTitle("Waiting for tag").setMessage(R.string.waiting_for_tag)
		// .create();

		// Upon interacting with UI controls, delay any scheduled hide()
		// operations to prevent the jarring behavior of controls going away
		// while interacting with the UI.
		Button writeTextButton = (Button) findViewById(R.id.write_text_button);
		writeTextButton.setOnTouchListener(mDelayHideTouchListener);
		writeTextButton.setOnClickListener(new OnClickListener() {

			@Override
			public void onClick(View v) {
				Log.d(TAG, "MainActivity.onCreate - writeTextButton clicked");
				if (mTag != null) {
					writeTagNewThread(mDefaultNdefTextMesssage, mTag);
				} else {
					logAndToast("Text write failed - tag not detected");
				}
			}
		});

		Button writeURLButton = (Button) findViewById(R.id.write_url_button);
		writeURLButton.setOnTouchListener(mDelayHideTouchListener);
		writeURLButton.setOnClickListener(new OnClickListener() {

			@Override
			public void onClick(View v) {
				Log.d(TAG, "MainActivity.onCreate - writeURLButton clicked.");
				if (mTag != null) {
					writeTagNewThread(mDefaultNdefURIMesssage, mTag);
				} else {
					logAndToast("URL write failed - tag not detected");
				}
			}
		});

		Button writeAARButton = (Button) findViewById(R.id.write_aar_button);
		writeAARButton.setOnTouchListener(mDelayHideTouchListener);
		writeAARButton.setOnClickListener(new OnClickListener() {

			@Override
			public void onClick(View v) {
				Log.d(TAG, "MainActivity.onCreate - writeAARButton clicked.");
				if (mTag != null) {
					writeTagNewThread(mAARTextMesssage, mTag);
				} else {
					logAndToast("AAR write failed - tag not detected");
				}
			}
		});

		mNfcPendingIntent = PendingIntent.getActivity(this, 0,
				new Intent(this, getClass()).addFlags(Intent.FLAG_ACTIVITY_SINGLE_TOP), 0);
		IntentFilter ndefFilter = new IntentFilter(NfcAdapter.ACTION_NDEF_DISCOVERED);
		try {
			ndefFilter.addDataType(TEXT_PLAIN_MIME_TYPE);
		} catch (MalformedMimeTypeException e) {
			e.printStackTrace();
			Log.e(TAG, "Error - MalformedMimeTypeException");
		}

		mNdefFilters = new IntentFilter[]{ndefFilter};

		mMode = WorkMode.MODE_READ;
	}

	@Override
	protected void onPostCreate(Bundle savedInstanceState) {
		super.onPostCreate(savedInstanceState);

		// Trigger the initial hide() shortly after the activity has been
		// created, to briefly hint to the user that UI controls
		// are available.
		delayedHide(100);
	}

	/**
	 * Touch listener to use for in-layout UI controls to delay hiding the
	 * system UI. This is to prevent the jarring behavior of controls going away
	 * while interacting with activity UI.
	 */
	View.OnTouchListener mDelayHideTouchListener = new View.OnTouchListener() {
		@Override
		public boolean onTouch(View view, MotionEvent motionEvent) {
			if (AUTO_HIDE) {
				delayedHide(AUTO_HIDE_DELAY_MILLIS);
			}
			return false;
		}
	};

	Handler mHideHandler = new Handler();
	Runnable mHideRunnable = new Runnable() {
		@Override
		public void run() {
			mSystemUiHider.hide();
		}
	};

	/**
	 * Schedules a call to hide() in [delay] milliseconds, canceling any
	 * previously scheduled calls.
	 */
	private void delayedHide(int delayMillis) {
		mHideHandler.removeCallbacks(mHideRunnable);
		mHideHandler.postDelayed(mHideRunnable, delayMillis);
	}

	private void logDetectedTechs(Tag pTag) {
		if (mTag != null) {
			for (String s : mTag.getTechList()) {
				Log.d(TAG, "Detected tech: " + s);
			}
		}
	}

	private void logTagInfo(Ndef pNdef) {
		if (pNdef != null) {
			int size = pNdef.getMaxSize(); // tag size
			boolean writable = pNdef.isWritable(); // is tag writable?
			String type = pNdef.getType(); // tag type
			Log.d(TAG, "Tag size: " + size + " type: " + type + " is writable?: " + writable);
			Log.d(TAG, "Tag can be made readonly: " + pNdef.canMakeReadOnly() + " is connected: " + pNdef.isConnected());
		}
	}

	@Override
	protected void onNewIntent(Intent intent) {
		Log.i(TAG, "MainActivity onNewIntent, action: " + intent.getAction());
		setIntent(intent);
		if (isNFCIntent(intent)) {
			mMode = WorkMode.MODE_READ;
		}
	}

	public void onPause() {
		super.onPause();
		mNfcAdapter.disableForegroundDispatch(this);
		Log.i(TAG, "MainActivity onPause");
	}

	public void onStop() {
		super.onStop();
		Log.i(TAG, "MainActivity onStop");
	}

	public void onRestart() {
		super.onRestart();
		Log.i(TAG, "MainActivity onRestart");
	}

	public void onStart() {
		super.onStart();
		Log.i(TAG, "MainActivity onStart");
	}

	public void onDestroy() {
		super.onDestroy();
		Log.i(TAG, "MainActivity onDestroy");
	}

	private boolean isNFCIntent(Intent pIntent) {
		String action = pIntent.getAction();
		return NfcAdapter.ACTION_NDEF_DISCOVERED.equals(action) || NfcAdapter.ACTION_TECH_DISCOVERED.equals(action)
				|| NfcAdapter.ACTION_TAG_DISCOVERED.equals(action);
	}

	private void handleNFCTag(Intent pNfcIntent) {
		if (!isNFCIntent(pNfcIntent)) {
			Log.w(TAG, "Non-NDEF action in intent - returning");
			return;
		} else {
			if (mMode == WorkMode.MODE_READ) {
				mTag = pNfcIntent.getParcelableExtra(NfcAdapter.EXTRA_TAG);
			} else {
				Tag newTag = pNfcIntent.getParcelableExtra(NfcAdapter.EXTRA_TAG);
				Log.i(TAG, "MainActivity newTag is null?: " + (newTag == null));

				if (newTag != null) {
					mTag = newTag;
				}
			}
			logDetectedTechs(mTag);

			if (mTag != null && mMode == WorkMode.MODE_READ) {
				mMode = WorkMode.MODE_WRITE;
				Ndef ndefTag = Ndef.get(mTag);

				if (ndefTag != null) {
					logTagInfo(ndefTag);
					NdefMessage ndefMesg = ndefTag.getCachedNdefMessage();
					if (ndefMesg != null) {
						displayMessages(ndefMesg.getRecords());
					} else {
						Log.w(TAG, "No cached NDEF message");
					}
				} else {
					Log.w(TAG, "ndefTag is null");
				}

				// if (NfcAdapter.ACTION_NDEF_DISCOVERED.equals(action)) {
				// Parcelable[] rawMsgs =
				// getIntent().getParcelableArrayExtra(NfcAdapter.EXTRA_NDEF_MESSAGES);
				//
				// if (rawMsgs != null) {
				// NdefMessage[] msgs = new NdefMessage[rawMsgs.length];
				//
				// for (int i = 0; i < rawMsgs.length; i++) {
				// msgs[i] = (NdefMessage) rawMsgs[i];
				// // Log.d(TAG, "NDEF message: " + msgs[i]);
				// }
				// Log.i(TAG, rawMsgs.length + " messages read.");
				// }
				// }
			}
		}
	}

	public void onResume() {
		super.onResume();
		// mDialog.hide();
		Intent nfcIntent = getIntent();
		Log.i(TAG, "MainActivity onResume, action: " + nfcIntent.getAction());
		setIntent(new Intent()); // consume Intent
		handleNFCTag(nfcIntent);

		String[][] techList = {new String[]{NfcA.class.getName()}, new String[]{MifareClassic.class.getName()}};
		mNfcAdapter.enableForegroundDispatch(this, mNfcPendingIntent, mNdefFilters, techList);
	}

	private void displayMessages(NdefRecord[] ndefRecords) {
		String[] rets = new String[ndefRecords.length];
		int i = 0;

		for (NdefRecord ndr : ndefRecords) {
			rets[i++] = parsePayload(ndr);
		}
		if (rets.length > 0) {
			updateTextField(rets[0]);
		}
	}

	private void updateTextField(final String text) {
		runOnUiThread(new Runnable() {

			@Override
			public void run() {
				TextView tv = (TextView) findViewById(R.id.fullscreen_content);
				tv.setText(text);
			}
		});
	}

	private String parseWellKnownPayload(NdefRecord pRecord) throws UnsupportedEncodingException {
		Log.d(TAG, "parseWellKnownPayload start");
		String ret = "";
		byte[] type = pRecord.getType();
		byte[] payload = pRecord.getPayload();

		if (Arrays.equals(type, NdefRecord.RTD_TEXT)) {
			Log.d(TAG, "NdefRecord.RTD_TEXT detected");
			if (payload.length > 0) {
				String textEncoding = ((payload[0] & 0200) == 0) ? "UTF-8" : "UTF-16";
				int languageCodeLength = payload[0] & 0077;
				String languageCode = new String(payload, 1, languageCodeLength, "US-ASCII");
				Log.d(TAG, "parseWellKnownPayload encoding: " + textEncoding + " languagecodelength: "
						+ languageCodeLength + " languageCode: " + languageCode);
				ret = new String(payload, languageCodeLength + 1, payload.length - languageCodeLength - 1, textEncoding);
				Log.d(TAG, "parseWellKnownPayload text: " + ret);
			}

			return ret;
		} else {// if (Arrays.equals(type, NdefRecord.RTD_URI)) {
			ret = parseUri(pRecord);

			return ret;
		}
	}

	private String parseUri(NdefRecord pNdefRecord) {
		String ret = "";
		if (isURLRecord(pNdefRecord)) {
			if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.JELLY_BEAN) {
				Uri u = pNdefRecord.toUri();
				if (u != null) {
					Log.d(TAG, "parseWellKnownPayload - URI detected");
					ret = u.toString();
					Intent i = new Intent(Intent.ACTION_VIEW);
					i.setData(u);
					startActivity(i);
				}
			} else {
				logAndToast("Intelligent URI parsing unsupported - API level 16 required!");
			}
		}

		return ret;
	}

	private boolean isURLRecord(NdefRecord pNdefRecord) {
		short tnf = pNdefRecord.getTnf();
		byte[] type = pNdefRecord.getType();

		if (NdefRecord.TNF_ABSOLUTE_URI == tnf
				|| (NdefRecord.TNF_WELL_KNOWN == tnf && (Arrays.equals(NdefRecord.RTD_URI, type) || Arrays.equals(
						NdefRecord.RTD_SMART_POSTER, type)))) {
			return true;
		} else {
			return false;
		}
	}

	private String normalizeMimeType(String pType) {
		if (pType == null) {
			return null;
		} else {
			pType = pType.trim().toLowerCase(Locale.US);
			int semicolonIndex = pType.indexOf(';');
			if (semicolonIndex >= 0) {
				pType = pType.substring(0, semicolonIndex);
			}

			return pType;
		}
	}

	private String detectMimeType(short pTnf, byte[] pType) {
		String ret = "";

		switch (pTnf) {
			case NdefRecord.TNF_WELL_KNOWN :
				if (Arrays.equals(pType, NdefRecord.RTD_TEXT)) {
					ret = TEXT_PLAIN_MIME_TYPE;
				}
				break;
			case NdefRecord.TNF_MIME_MEDIA :
				String mimeType = new String(pType, Charset.forName("US_ASCII"));
				ret = normalizeMimeType(mimeType);
		}

		return ret;
	}

	private String parseMimeMediaPayload(NdefRecord pRecord) throws UnsupportedEncodingException {
		String ret = "";
		String mimeType = detectMimeType(pRecord.getTnf(), pRecord.getType());
		if (!TEXT_PLAIN_MIME_TYPE.equals(mimeType)) {
			Log.w(TAG, "parseMimeMediaPayload - unsupported mime type detected: " + mimeType);
			return "";
		}

		byte[] payload = pRecord.getPayload();
		Log.d(TAG, "parseMimeMediaPayload mimeType: " + mimeType + " payload length: " + payload.length);

		if (payload.length > 0) {
			ret = new String(payload);
			Log.d(TAG, "parseMimeMediaPayload Text: " + ret);
		}

		return ret;
	}

	private String parsePayload(NdefRecord pRecord) {
		Log.d(TAG, "parsePayload start, TNF: " + pRecord.getTnf() + " type: " + pRecord.getType());
		String ret = "";

		// TNF values supported by this application:
		switch (pRecord.getTnf()) {
			case NdefRecord.TNF_WELL_KNOWN :
				try {
					ret = parseWellKnownPayload(pRecord);
				} catch (UnsupportedEncodingException e) {
					Log.e(TAG, "parsePayload TNF_WELL_KNOWN - UnsupportedEncodingException");
					e.printStackTrace();
				}
				break;

			case NdefRecord.TNF_MIME_MEDIA :
				try {
					ret = parseMimeMediaPayload(pRecord);
				} catch (UnsupportedEncodingException e) {
					Log.e(TAG, "parsePayload TNF_MIME_MEDIA - UnsupportedEncodingException");
					e.printStackTrace();
				}
				break;

			case NdefRecord.TNF_ABSOLUTE_URI :
				ret = parseUri(pRecord);
				// Log.w(TAG, "Unsupported NdefRecord type detected: " +
				// NdefRecord.TNF_ABSOLUTE_URI);
				break;

			case NdefRecord.TNF_EXTERNAL_TYPE :
				ret = parseUri(pRecord);
				// Log.w(TAG, "Unsupported NdefRecord type detected: " +
				// NdefRecord.TNF_EXTERNAL_TYPE);
				break;
		}

		return ret;
	}

	private void writeTagNewThread(final NdefMessage pMessage, final Tag pTag) {
		new Thread(new Runnable() {

			@Override
			public void run() {
				writeTag(pMessage, pTag);
			}
		}).start();
	}

	private boolean writeTag(final NdefMessage pMessage, final Tag pTag) {
		boolean ret = false;

		if (pTag == null) {
			logAndToast("Write failed - no tag detected");
			return false;
		}
		int messageSize = pMessage.toByteArray().length;

		NdefFormatable nf = NdefFormatable.get(pTag);
		Ndef ndef = Ndef.get(pTag);

		synchronized (syncObject) {
			Log.i(TAG, "writeTag start, message size: " + messageSize);

			try {
				if (nf != null) {
					Log.d(TAG, "writeTag - NdefFormatable Tag detected");
					nf.connect();
					nf.format(pMessage);
					logAndToast("Write completed");

					ret = true;
				} else if (ndef != null) {
					ndef.connect();
					if (messageSize > ndef.getMaxSize()) {
						logAndToast("Write failed - message size exceeds tag size");
						ret = false;
					}
					if (!ndef.isWritable()) {
						logAndToast("Write failed - tag is not writable");
						ret = false;
					}

					ndef.writeNdefMessage(pMessage);
					logAndToast("Write completed");

					ret = true;
				} else {
					logAndToast("Write failed - unsupported tag");
					ret = false;
				}
			} catch (TagLostException e) {
				mTag = null; // forget the tag
				logAndToast("Write failed - TagLostException: " + e.getMessage());
				e.printStackTrace();

				ret = false;
			} catch (IOException e) {
				mTag = null; // forget the tag
				logAndToast("Write failed - IOException: " + e.getMessage());
				e.printStackTrace();

				ret = false;
			} catch (FormatException e) {
				logAndToast("Write failed - FormatException: " + e.getMessage());
				e.printStackTrace();

				ret = false;
			} finally {
				try {
					if (nf != null) {
						nf.close();
					}
					if (ndef != null) {
						ndef.close();
					}
				} catch (IOException e) {
					Log.e(TAG, "Exception while closing");
					e.printStackTrace();
				}
			}
		}

		return ret;
	}

	private void logAndToast(final String pMessage) {
		Log.i(TAG, pMessage);
		toast(pMessage);
	}

	private void toast(final String pMessage) {
		runOnUiThread(new Runnable() {

			@Override
			public void run() {
				Toast.makeText(MainActivity.this.getApplicationContext(), pMessage, Toast.LENGTH_SHORT).show();
			}
		});
	}

}
