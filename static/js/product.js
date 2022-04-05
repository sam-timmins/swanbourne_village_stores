
const increaseCounterRef = document.querySelector(".increase-counter");
const decreaseCounterRef = document.querySelector(".decrease-counter");
const itemQuantityRef = document.querySelector(".item-quantity");


window.onload = function () {

    increaseCounter = () => {

        let quantity = itemQuantityRef.value

        quantity++;
        itemQuantityRef.value = quantity;

        if (quantity >= 1) {
            decreaseCounterRef.style.display = 'flex'
        }

    };

    decreaseCounter = () => {

        let quantity = itemQuantityRef.value

        quantity--;
        itemQuantityRef.value = quantity;

        if (quantity == 0) {
            decreaseCounterRef.style.display = 'none'
        }

    };

    increaseCounterRef.addEventListener('click', increaseCounter)
    decreaseCounterRef.addEventListener('click', decreaseCounter)
};