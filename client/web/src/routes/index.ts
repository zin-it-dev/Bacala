const routes = [
  { path: "/", component: () => import("@/pages/Home.vue") },
  { path: "/about", component: () => import("@/pages/About.vue") },
];

export default routes;
