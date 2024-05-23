import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'
import piniaPluginPersistedstate from 'pinia-plugin-persistedstate'
import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/js/bootstrap.bundle.min.js';

const pinia = createPinia();

const app = createApp(App)
pinia.use(piniaPluginPersistedstate)

app.use(createPinia())
app.use(router)

app.mount('#app')
