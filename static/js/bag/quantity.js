window.onload = function () {

    const increaseCounterRef = document.querySelectorAll(".increase-counter");
    const decreaseCounterRef = document.querySelectorAll(".decrease-counter");

    const lowestQuantity = 1;
    const highestQuantity = 25  ;

    /**
     * Hides the increase counter and shows helper text if the
     * quantity value is greater than 25.
     * Shows the increase counter if the quantity is greater than or equal to 1
     */
    increaseCounterRef.forEach( counter => {
        counter.addEventListener(
            'click', () => {
                let quantityContainer = counter.parentElement;
                let formItems = quantityContainer.children;
                let helperText = quantityContainer.nextElementSibling;
                let decreaseCounter = formItems[0];
                let quantityValue = formItems[1];
                let quantity = quantityValue.value;
                    
                quantity++;
                quantityValue.value = quantity;

                if (quantity >= lowestQuantity) {
                    decreaseCounter.style.setProperty("display", "flex", "important");
                }
                    
                if (quantity >= highestQuantity) {
                    counter.style.display = 'none';
                    helperText.style.setProperty("display", "inline", "important");
                }
            }
        );
    });

    /**
     * Shows the increase counter and hides helper text if the
     * quantity value is less than or equal to 25.
     * Hides the decrease counter if the quantity is less than or equal to 1
     */

    decreaseCounterRef.forEach( counter => {
        counter.addEventListener(
            'click', () => {
                let quantityContainer = counter.parentElement;
                let formItems = quantityContainer.children;
                let helperText = quantityContainer.nextElementSibling;
                let quantityValue = formItems[1];
                let increase = formItems[2];
                let quantity = quantityValue.value;

                quantity--;
                quantityValue.value = quantity;

                if (quantity <= lowestQuantity) {
                    counter.style.display = 'none';
                }
                
                if (quantity <= highestQuantity) {
                    increase.style.display = 'flex';
                    helperText.style.setProperty("display", "none", "important");
                }
            }
        );
    });
};
    