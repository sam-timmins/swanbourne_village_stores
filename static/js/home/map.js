    // Google maps display
    function initMap() {
        const options = {
            zoom: 14,
            center: {
                lat: 51.938492,
                lng: -0.834284,
            },
            disableDefaultUI: true,
            scaleControl: true,
            fullscreenControl: true,
            gestureHandling: "none",
        }

        const map = new google.maps.Map(document.querySelector("#map"), options);

        // Position the marker
        const marker = new google.maps.Marker({
            position: {
                lat: 51.938492,
                lng: -0.834284,
            },
            map: map,
        });
    }