
document.addEventListener("DOMContentLoaded", function () {

    // Maximum upload size: 50 MB
    const MAX_FILE_SIZE = 50 * 1024 * 1024;

    // Supported image extensions
    const ALLOWED_EXTENSIONS = [
        ".tif",
        ".tiff",
        ".png",
        ".jpg",
        ".jpeg"
    ];

    // Validate uploaded files
    function validateFile(file) {

        if (!file) {
            return "Please select a file.";
        }

        const extension = file.name
            .substring(file.name.lastIndexOf("."))
            .toLowerCase();

        if (!ALLOWED_EXTENSIONS.includes(extension)) {
            return "Unsupported image format.";
        }

        if (file.size > MAX_FILE_SIZE) {
            return "File size must be less than 50 MB.";
        }

        if (file.size === 0) {
            return "The selected file is empty.";
        }

        return null;
    }


    // Show validation messages
    function showMessage(form, message) {

        let messageBox = form.querySelector(
            ".client-message"
        );

        if (!messageBox) {

            messageBox = document.createElement("div");

            messageBox.className = "client-message";

            messageBox.style.color = "#ff8195";
            messageBox.style.fontSize = "12px";
            messageBox.style.marginTop = "12px";

            form.appendChild(messageBox);
        }

        messageBox.textContent = message;
    }


    // Validate image upload forms
    const uploadForms = document.querySelectorAll(
        'form[enctype="multipart/form-data"]'
    );

    uploadForms.forEach(function (form) {

        const fileInputs = form.querySelectorAll(
            'input[type="file"]'
        );

        fileInputs.forEach(function (input) {

            input.addEventListener("change", function () {

                const file = input.files[0];

                if (!file) {
                    return;
                }

                const error = validateFile(file);

                if (error) {

                    showMessage(form, error);

                    input.value = "";

                    return;
                }

                const messageBox = form.querySelector(
                    ".client-message"
                );

                if (messageBox) {
                    messageBox.remove();
                }

                showMessage(
                    form,
                    "Selected: " + file.name
                );

                const uploadArea = input.closest(
                    ".upload-area"
                );

                if (uploadArea) {

                    const title = uploadArea.querySelector(
                        "strong"
                    );

                    if (title) {
                        title.textContent = file.name;
                    }
                }

            });

        });


        // Prevent repeated form submission
        form.addEventListener("submit", function (event) {

            let hasError = false;

            fileInputs.forEach(function (input) {

                const file = input.files[0];

                const error = validateFile(file);

                if (error) {

                    showMessage(form, error);

                    hasError = true;
                }

            });

            if (hasError) {
                event.preventDefault();
                return;
            }

            const button = form.querySelector(
                'button[type="submit"]'
            );

            if (button) {

                button.disabled = true;

                button.textContent = "Processing...";

            }

        });

    });


    // Smooth scrolling for dashboard sections
    document.querySelectorAll(
        'a[href^="#"]'
    ).forEach(function (link) {

        link.addEventListener("click", function (event) {

            const target = document.querySelector(
                link.getAttribute("href")
            );

            if (target) {

                event.preventDefault();

                target.scrollIntoView({
                    behavior: "smooth"
                });

            }

        });

    });


    console.log(
        "AI Satellite Intelligence System initialized."
    );

});
