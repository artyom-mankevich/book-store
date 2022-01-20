let updateBtns = document.getElementsByClassName('update-cart');
let saveBtns = document.getElementsByClassName('save-order');

for (let i = 0; i < updateBtns.length; i++) {
    updateBtns[i].addEventListener('click', function () {
        let productId = this.dataset.product
        let action = this.dataset.action

        if (user !== 'AnonymousUser') {
            updateUserOrder(productId, action)
        }
    })
}

for (let i = 0; i < saveBtns.length; i++) {
    saveBtns[i].addEventListener('click', function () {
        let orderId = this.dataset.order
        let action = this.dataset.action

        if (user !== 'AnonymousUser') {
            saveOrder(orderId, action)
        }
    })
}

function updateUserOrder(productId, action) {
    let url = '/update_item/'

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken
        },
        body: JSON.stringify({'productId': productId, 'action': action})
    })
        .then((response) => {
            return response.json()
        })
        .then(() => {
            location.reload()
        })
}

function saveOrder(orderId, action) {
    let url = '/save_order/'

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken
        },
        body: JSON.stringify({'orderId': orderId, 'action': action})
    })
        .then((response) => {
            return response.json()
        })
        .then(() => {
            location.reload()
        })
}