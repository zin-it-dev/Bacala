/**
 * plugins/index.ts
 *
 * Automatically included in `./src/main.ts`
 */

// Plugins
import vuetify from "./vuetify";
import router from "./router";

// Types
import type { App } from "vue";
import { VueQueryPlugin } from '@tanstack/vue-query'

export function registerPlugins(app: App) {
  app.use(VueQueryPlugin)
  app.use(vuetify);
  app.use(router);
}
