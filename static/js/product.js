
const increaseCounterRef = document.querySelector(".increase-counter");
const decreaseCounterRef = document.querySelector(".decrease-counter");
const itemQuantityRef = document.querySelector(".item-quantity");


window.onload = function () {

    increaseCounterRef.addEventListener('click', () => {

        let quantity = itemQuantityRef.value

        quantity++;
        itemQuantityRef.value = quantity;

        if (quantity >= 1) {
            decreaseCounterRef.style.display = 'flex'
        }
        
        if (quantity > 24) {
            increaseCounterRef.style.display = 'none'
        }

    });

    decreaseCounterRef.addEventListener('click', () => {

        let quantity = itemQuantityRef.value

        quantity--;
        itemQuantityRef.value = quantity;

        if (quantity == 0) {
            decreaseCounterRef.style.display = 'none'
        }
        
        if (quantity < 26) {
            increaseCounterRef.style.display = 'flex'
        }

    });

};