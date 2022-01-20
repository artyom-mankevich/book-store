validateUsername();
validateEmail();
validateName('first');
validateName('last');
validateImage()

function validateUsername() {
    const username = document.getElementById('id_username');
    const usernameRegEx = /^[a-z0-9_]{3,30}$/

    username.oninput = function () {
        if (username.validity.tooShort) {
            username.setCustomValidity('Username is too short')
        } else if (username.validity.tooLong) {
            username.setCustomValidity('Username is too long')
        } else if (!usernameRegEx.test(username.value)) {
            username.setCustomValidity('Incorrect username')
        } else {
            username.setCustomValidity('')
        }
    }
}

function validateEmail() {
    const email = document.getElementById('id_email');

    email.oninput = function () {
        if (email.validity.typeMismatch) {
            email.setCustomValidity('Not a valid email address');
        } else {
            email.setCustomValidity('')
        }
    }
}

function validateName(inputId) {
    const name = document.getElementById(`id_${inputId}_name`);
    const nameRegEx = /^[A-Z][a-z]+$/

    name.oninput = function () {
        if (name.value.trim() !== '') {
            if (!nameRegEx.test(name.value)) {
                name.setCustomValidity(`Invalid ${inputId} name`);
            } else {
                name.setCustomValidity('')
            }
        }
    }
}

function validateImage() {
    const file_input = document.getElementById('id_profile_pic')

    file_input.oninput = function () {
        if (file_input.files[0]) {
            const file = file_input.files[0];
            let image = new Image();
            image.onload = function () {
                file_input.setCustomValidity('')
            }
            image.onerror = function () {
                file_input.setCustomValidity('Only images are allowed')
            }
            const url = window.URL || window.webkitURL
            image.src = url.createObjectURL(file);
            URL.revokeObjectURL(image.src)
            if (file.size > 2.5 * 1024 * 1024) {
                file_input.setCustomValidity('File is too big')
            }
        }
    }
}