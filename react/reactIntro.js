function Button(props) {
  return (
    <button onClick={() => props.onClickFunction(props.increment)}>
      +{props.increment}
    </button>
  );
}

function Display(props) {
  return <div>{props.message}</div>;
}

function App() {
  const [counter, setCounter] = useState(42);
  const incrementCounter = incrementValue =>
    setCounter(counter + incrementValue);
  return (
    <div>
      <Button onClickFunction={incrementCounter} increment={1} />
      <Button onClickFunction={incrementCounter} increment={5} />
      <Button onClickFunction={incrementCounter} increment={10} />
      <Button onClickFunction={incrementCounter} increment={15} />
      <Display message={counter} />
    </div>
  );
}

ReactDOM.render(<App />, document.getElementById("mountNode"));

setInterval(() => {
  document.getElementById(
    "mountNode"
  ).innerHTML = `<div><h1>Hello HTML</h1><input type="text"/><pre>${new Date().toLocaleTimeString()}</pre></div>`;
  ReactDOM.render(
    React.createElement(
      "div",
      null,
      React.createElement("h1", null, "Hello HTML"),
      React.createElement("input", null),
      React.createElement("pre", null, new Date().toLocaleTimeString())
    ),
    document.getElementById("mountNode2")
  );
}, 1000);
