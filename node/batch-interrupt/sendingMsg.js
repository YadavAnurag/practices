const accountSID = 'ACc76494ec9ad6c86fd99b559c6b98ee23'
const authTocken = 'd560af6d4c812fa3ed96e1b727a2f987'

const twilio = require('twilio')
const twilioClient = twilio(accountSID, authTocken)

twilioClient.messages.
    create({
        body: 'Hi this is anurag yadav',
        from: 'whatsapp:+14155238886',
        to: 'whatsapp:+918127676840'
    })
    .then(msg => console.log(msg.sid))
    .done()
    