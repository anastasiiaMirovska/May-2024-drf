import React from 'react';
import PizzaForm from "../components/PizzaForm";
import PizzasComponent from "../components/Pizzas/PizzasComponent";
import Chat from "../components/Chat";


const PizzasPage = () => {
    return (
        <div>
            <PizzaForm/>
            <hr/>
            <PizzasComponent/>
            <hr/>
            <Chat/>
            <hr/>
        </div>
    );
};

export default PizzasPage;