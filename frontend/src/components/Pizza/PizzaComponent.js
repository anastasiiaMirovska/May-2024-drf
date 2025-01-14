import React from 'react';

const PizzaComponent = ({pizza}) => {
    return (
        <div>
            {JSON.stringify(pizza)}
        </div>
    );
};

export default PizzaComponent;