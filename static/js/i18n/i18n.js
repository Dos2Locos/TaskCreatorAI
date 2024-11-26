// Create a global i18n instance
window.i18n = new class I18n {
    constructor() {
        this.currentLocale = localStorage.getItem('locale') || 'en-GB';
        this.translations = {
            'en-GB': enGB,
            'es-ES': esES,
            'zh-CN': zhCN
        };
        this.availableLocales = Object.keys(this.translations);
    }

    setLocale(locale) {
        if (this.availableLocales.includes(locale)) {
            this.currentLocale = locale;
            localStorage.setItem('locale', locale);
            this.updatePageTranslations();
            return true;
        }
        return false;
    }

    t(key) {
        return this.translations[this.currentLocale][key] || key;
    }

    updatePageTranslations() {
        // Update all elements with data-i18n attribute
        document.querySelectorAll('[data-i18n]').forEach(element => {
            const key = element.getAttribute('data-i18n');
            if (key) {
                if ((element.tagName === 'INPUT' && element.getAttribute('type') === 'text') || 
                    element.tagName === 'TEXTAREA') {
                    element.placeholder = this.t(key);
                } else {
                    element.textContent = this.t(key);
                }
            }
        });

        // Update HTML lang attribute
        document.documentElement.lang = this.currentLocale;

        // Dispatch event for components that need to know about language changes
        window.dispatchEvent(new CustomEvent('languageChanged', {
            detail: { locale: this.currentLocale }
        }));
    }

    getCurrentLocale() {
        return this.currentLocale;
    }

    getAvailableLocales() {
        return this.availableLocales.map(locale => ({
            code: locale,
            name: this.translations[locale]['language.name']
        }));
    }
}();
