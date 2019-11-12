
#include<bits/stdc++.h>
using namespace std;


class CoffeeMachine{
    private:
        static CoffeeMachine* uniqueInstance;
        CoffeeMachine() {}
    public:
        map<string, int> beverageList, ingredientList;
        static CoffeeMachine* getInstance(){
            if(!uniqueInstance){
                uniqueInstance = new CoffeeMachine();
            }
            return uniqueInstance;
        } 
};

CoffeeMachine *CoffeeMachine::uniqueInstance = 0;


class Beverages{
    public:
        string description = "No coffe";
    public:
        virtual void addBeverage() = 0;
        virtual int getCost() = 0;
        virtual string getDescription(){
            return description;
        }
};

class Cappuccino : public Beverages{
    public:
        Cappuccino(){
            description = "Cappuccino";
        }
        void addBeverage(){
            CoffeeMachine *coffeeMachine = CoffeeMachine::getInstance();
            coffeeMachine->beverageList.insert(make_pair("Cappuccino", 12));
        }
        int getCost(){
            CoffeeMachine *coffeeMachine = CoffeeMachine::getInstance();
            return coffeeMachine->beverageList["Cappuccino"];
        }
        
};

class Espresso : public Beverages{
    public:
        Espresso(){
            description = "Espresso";
        }
        void addBeverage(){
            CoffeeMachine *coffeeMachine = CoffeeMachine::getInstance();
            coffeeMachine->beverageList.insert(make_pair("Espresso", 15));
        }
        int getCost(){
            CoffeeMachine *coffeeMachine = CoffeeMachine::getInstance();
            return coffeeMachine->beverageList["Espresso"];
        }
};


class Ingredients : public Beverages{
    public:
        virtual void addIngredient() = 0;
        virtual string getDescription() = 0;
        void addBeverage(){
            //No use of addBeverage
        }
};

class Sugar : public Ingredients{
    Beverages *coffee;

    public:
        Sugar(){
            this->coffee = NULL;
        }
        Sugar (Beverages* coffee){
            this->coffee = coffee;
        }
        void addIngredient(){
            CoffeeMachine *coffeeMachine = CoffeeMachine::getInstance();
            coffeeMachine->ingredientList.insert(make_pair("Sugar", 2));
        }
        string getDescription(){
            return coffee->getDescription()+" with Sugar";
        }
        int getCost(){
            CoffeeMachine *coffeeMachine = CoffeeMachine::getInstance();
            return coffee->getCost()+coffeeMachine->ingredientList["Sugar"];
        }
};

class Cream : public Ingredients{
    Beverages *coffee;

    public:
        Cream(){
            this->coffee = NULL;
        }
        Cream(Beverages* coffee){
            this->coffee = coffee;
        }
        void addIngredient(){
            CoffeeMachine *coffeeMachine = CoffeeMachine::getInstance();
            coffeeMachine->ingredientList.insert(make_pair("Cream", 5));
        }

        string getDescription(){
            return coffee->getDescription()+" with Cream";
        }

        int getCost(){
            CoffeeMachine *coffeeMachine = CoffeeMachine::getInstance();
            return coffee->getCost()+coffeeMachine->ingredientList["Cream"];
        }
};

void prepareMenu(){
    Cappuccino *cappuccino = new Cappuccino();
    cappuccino->addBeverage();
    Espresso *espresso = new Espresso();
    espresso->addBeverage();
    Sugar *sugar = new Sugar();
    sugar->addIngredient();
    Cream *cream = new Cream();
    cream->addIngredient();
}

void displayBeverages(){
    CoffeeMachine *coffeMachine = CoffeeMachine::getInstance();
    cout<<"Coffee\t\tPrice"<<endl<<endl;
    int index = 1;
    for(auto x:coffeMachine->beverageList)
        cout<<index++<<"."<<x.first<<"\t"<<x.second<<endl;
    cout<<endl<<endl;
}

void displayIngredients(){
    CoffeeMachine *coffeMachine = Cof
feeMachine::getInstance();
    cout<<"Ingredients\tPrice"<<endl<<endl;
    int index = 1;
    for(auto x:coffeMachine->ingredientList)
        cout<<index++<<"."<<x.first<<"\t\t"<<x.second<<endl;

}
int main(){
    prepareMenu();
    displayBeverages();
    displayIngredients();
    while(true){
        cout<<endl<<"Select coffee from the given List ans press q to exit"<<endl;
        char inp;
        cin>>inp;
        if(inp=='q' || inp=='Q')
            break;
        Beverages *coffee;
        if(inp=='1'){
            coffee = new Cappuccino();
            cout<<"Cappuccino selected"<<endl<<endl;
        }
        else if(inp=='2'){
            coffee = new Espresso();
            cout<<"Espresso selected"<<endl<<endl;
        }
        else{
            cout<<"Invalid Input"<<endl;
            continue;
        }
        cout<<"Select Ingredients or press q to exit"<<endl;
        while(true){
            cin>>inp;
            if(inp=='q' || inp=='Q')
                break;
            if(inp=='1'){
                coffee = new Cream(coffee);
                cout<<"Cream selected"<<endl;
            }
            else if(inp=='2'){
                coffee = new Sugar(coffee);
                cout<<"Sugar selected"<<endl;
            }
            else{
                cout<<"Invalid Input"<<endl;
                continue;
            }
        }
        cout<<"Your "<<coffee->getDescription()<<" is ready"<<endl;
        cout<<"Total cost is "<<coffee->getCost()<<endl;
    }
}
