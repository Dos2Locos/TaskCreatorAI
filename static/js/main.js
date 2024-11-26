class TaskTransformer {
    constructor() {
        // Get the global i18n instance
        this.i18n = window.i18n;
        
        // Initialize DOM elements
        this.elements = {
            taskInput: document.getElementById('task-input'),
            resultArea: document.getElementById('result'),
            spinner: document.getElementById('spinner'),
            button: document.getElementById('transform-btn'),
            resultContainer: document.getElementById('result-container'),
            errorMessage: document.getElementById('error-message'),
            languageSelect: document.getElementById('language-select'),
            copyButton: document.getElementById('copy-button')
        };
        
        // Bind methods to preserve context
        this.transform = this.transform.bind(this);
        this.handleError = this.handleError.bind(this);
        this.handleLanguageChange = this.handleLanguageChange.bind(this);
        this.handleCopy = this.handleCopy.bind(this);
        
        // Initialize language selector
        this.initializeLanguageSelector();
        
        // Add event listeners
        this.elements.button.addEventListener('click', this.transform);
        this.elements.taskInput.addEventListener('input', () => {
            this.clearError();
            this.clearResult();
        });
        this.elements.languageSelect.addEventListener('change', this.handleLanguageChange);
        this.elements.copyButton.addEventListener('click', this.handleCopy);

        // Initialize Prism.js
        if (window.Prism) {
            Prism.highlightAll();
        }

        // Initial translation
        this.i18n.updatePageTranslations();
    }

    initializeLanguageSelector() {
        const locales = this.i18n.getAvailableLocales();
        const currentLocale = this.i18n.getCurrentLocale();
        
        // Clear any existing options
        this.elements.languageSelect.innerHTML = '';
        
        // Add new options
        locales.forEach(locale => {
            const option = document.createElement('option');
            option.value = locale.code;
            option.textContent = locale.name;
            option.selected = locale.code === currentLocale;
            this.elements.languageSelect.appendChild(option);
        });
    }

    handleLanguageChange(event) {
        const newLocale = event.target.value;
        this.i18n.setLocale(newLocale);
    }

    clearError() {
        this.elements.errorMessage.style.display = 'none';
        this.elements.errorMessage.textContent = '';
    }

    clearResult() {
        this.elements.resultArea.textContent = '';
        this.elements.resultContainer.style.display = 'none';
    }

    setLoading(isLoading) {
        const { button, taskInput, spinner, resultContainer } = this.elements;
        
        button.disabled = isLoading;
        taskInput.disabled = isLoading;
        spinner.style.display = isLoading ? 'block' : 'none';
        
        if (isLoading) {
            resultContainer.classList.add('fade');
            button.innerHTML = `<span>${this.i18n.t('transform.processing')}</span>`;
        } else {
            resultContainer.classList.remove('fade');
            button.innerHTML = `<span>${this.i18n.t('transform.button')}</span>`;
        }
    }

    handleError(message) {
        const { errorMessage, resultContainer } = this.elements;
        errorMessage.textContent = message;
        errorMessage.style.display = 'block';
        resultContainer.style.display = 'none';
    }

    displayResult(data) {
        const { resultArea, resultContainer } = this.elements;
        resultArea.textContent = JSON.stringify(data, null, 2);
        resultContainer.style.display = 'block';
        if (window.Prism) {
            Prism.highlightElement(resultArea);
        }
    }

    async handleCopy() {
        const { copyButton, resultArea } = this.elements;
        try {
            await navigator.clipboard.writeText(resultArea.textContent);
            const originalText = copyButton.textContent;
            copyButton.textContent = this.i18n.t('copy.success');
            copyButton.classList.add('copied');
            setTimeout(() => {
                copyButton.textContent = this.i18n.t('copy.button');
                copyButton.classList.remove('copied');
            }, 2000);
        } catch (err) {
            console.error('Failed to copy text:', err);
        }
    }

    async transform() {
        const { taskInput } = this.elements;
        const taskText = taskInput.value.trim();

        if (!taskText) {
            this.handleError(this.i18n.t('error.empty_input'));
            return;
        }

        this.setLoading(true);
        this.clearError();

        try {
            const response = await fetch('/transform', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Accept': 'application/json'
                },
                body: JSON.stringify({ task: taskText })
            });

            const data = await response.json();

            if (response.ok) {
                this.displayResult(data);
            } else {
                throw new Error(data.error || this.i18n.t('error.transform_failed'));
            }
        } catch (error) {
            const errorMessage = error.message === 'Failed to fetch'
                ? this.i18n.t('error.network')
                : `${this.i18n.t('error.transform_failed')}: ${error.message}`;
            this.handleError(errorMessage);
        } finally {
            this.setLoading(false);
        }
    }
}

// Initialize the application when the DOM is fully loaded
document.addEventListener('DOMContentLoaded', () => {
    new TaskTransformer();
});
