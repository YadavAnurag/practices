class Person {
    firstName: string;
    lastName: string;
    age: number;

    constructor(firstName: string, lastName: string, age?: number) {
        this.firstName = firstName;
        this.lastName = lastName;
        this.age = age || 0;
    }

    greet(): void {
        console.log(`Hello ${this.firstName} ${this.lastName}`);
    }

    ageInYears(years: number): number {
        return this.age + years;
    }

}

var person: Person = new Person('Anu', 'Yadav');

person.greet();