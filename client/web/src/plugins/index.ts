/**
 * plugins/index.ts
 *
 * Automatically included in `./src/main.ts`
 */

// Plugins
import vuetify from "./vuetify";
import router from "./router";
import { firebaseApp } from "./firebase";

// Types
import type { App } from "vue";
import { VueQueryPlugin } from "@tanstack/vue-query";
import { VueFire, VueFireAuth } from "vuefire";

export function registerPlugins(app: App) {
  app.use(VueQueryPlugin);
  app.use(vuetify);
  app.use(router);
  app.use(VueFire, {
    firebaseApp,
    modules: [VueFireAuth()],
  });
}
