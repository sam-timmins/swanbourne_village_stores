window.onload = function () {

    const increaseCounterRef = document.querySelector(".increase-counter");
    const decreaseCounterRef = document.querySelector(".decrease-counter");
    const itemQuantityRef = document.querySelector(".item-quantity");
    const quantityHelperRef = document.querySelector(".quantity-helper");
    const submitQuantityRef = document.querySelector(".submit-quantity");

    const lowestQuantity = 1
    const highestQuantity = 25  

    /**
     * Hides the increase and the submit button and shows helper text if the
     * quantity value is greater than 25.
     * Shows the increase button if the quantity is greater than or equal to 1
     */
    increaseCounterRef.addEventListener('click', () => {

        let quantity = itemQuantityRef.value
        quantity++;
        itemQuantityRef.value = quantity;

        if (quantity >= lowestQuantity) {
            decreaseCounterRef.style.setProperty("display", "flex", "important")
        }
        
        if (quantity >= highestQuantity) {
            increaseCounterRef.style.display = 'none'
            submitQuantityRef.style.opacity = "0"
            quantityHelperRef.style.setProperty("display", "inline", "important")
        }
    });

    /**
     * Shows the increase and the submit button and hides helper text if the
     * quantity value is less than or equal to 25.
     * Hides the decrease button if the quantity is less than or equal to 1
     */
    decreaseCounterRef.addEventListener('click', () => {

        let quantity = itemQuantityRef.value
        quantity--;
        itemQuantityRef.value = quantity;

        if (quantity <= lowestQuantity) {
            decreaseCounterRef.style.display = 'none'
        }

        if (quantity <= highestQuantity) {
            increaseCounterRef.style.display = 'flex'
            quantityHelperRef.style.setProperty("display", "none", "important")
            submitQuantityRef.style.opacity = "1"
        }
    });

};