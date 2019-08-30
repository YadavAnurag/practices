import React, { Component } from 'react';
import './App.css';


class App extends Component {
  render() {

    var helloWorld = `Welcome to the "Road to learn React"`;

    class Person {
      firstName = 'luna';
      lastName = 'oscura';

      constructor(user) {
        this.firstName = user.firstName;
        this.lastName = user.lastName;
      }

      setName(user) {
        this.firstName = user.firstName;
        this.lastName = user.lastName;
      }
    }
    Person.prototype.toString = function () { return `${this.firstName} ${this.lastName}`; }

    var kushwaha = new Person({ firstName: 'luna', lastName: 'oscura' });
    kushwaha.setName({ firstName: 'Shivam', lastName: 'Verma' });


    const list = [
      {
        title: 'React',
        url: 'https://facebook.github.io/react',
        author: 'Jordan Walke',
        num_comments: 3,
        points: 4,
        objectID: 0,
      },
      {
        title: 'Redux',
        url: 'https://facebook.github.io/redux',
        author: 'Dan Abarmov, Andrew Clark',
        num_comments: 2,
        points: 5,
        objectID: 1,
      }
    ];

    return (
      <div className="App">
        {list.map(item => {
          return (
            <div key={item.objectID}>
              <span>
                <a href={item.url}>{item.title}</a>
              </span> <br />
              <span>{item.author}</span>
              <span>{item.num_comments}</span>
              <span>{item.points}</span>
            </div>
          );
        }
        )}
      </div>
    );
  }
}


export default App;
