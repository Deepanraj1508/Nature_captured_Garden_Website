let menu = document.querySelector(".hamburger-menu");
let nav = document.querySelector("#menu");

menu.addEventListener('click', function (event) {
    // document.querySelector('#menu').setAttribute("class", "menu-toggle");
    // console.log("ok")
    nav.classList.toggle("menu-toggle");
});

document.addEventListener('DOMContentLoaded', function () {
    const addToCartButtons = document.querySelectorAll('.add-to-cart');
    
    addToCartButtons.forEach(button => {
        button.addEventListener('click', showProductDetails);
    });

    function showProductDetails(event) {
        const product = event.target.closest('.item-details');
        const productId = product.dataset.id;
        const productName = product.querySelector('p').textContent;
        const productPrice = product.querySelector('.price').textContent;

        // Display product details in a modal
        displayModal(productId, productName, productPrice);
    }

    function displayModal(productId, productName, productPrice) {
        const modal = document.getElementById('product-modal');
        const modalOverlay = document.getElementById('modal-overlay');
        const modalContent = document.getElementById('modal-content');

        modalContent.innerHTML = `
            <h2>Cart Item</h2>
            <p><strong>ID:</strong> ${productId}</p>
            <p><strong>Name:</strong> ${productName}</p>
            <p><strong>Price:</strong> ${productPrice}</p>
        `;

        modal.style.display = 'block';
        modalOverlay.style.display = 'block';

        modalOverlay.addEventListener('click', hideModal);
    }

    function hideModal() {
        const modal = document.getElementById('product-modal');
        const modalOverlay = document.getElementById('modal-overlay');

        modal.style.display = 'none';
        modalOverlay.style.display = 'none';
    }
});


