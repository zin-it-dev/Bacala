<script setup lang="ts">
import { useQuery } from "@tanstack/vue-query";

import { getCategories } from "@/services/category.service";

const { data } = useQuery({
  queryKey: ["categories"],
  queryFn: getCategories,
});
</script>

<template>
  <v-app-bar :elevation="2" rounded>
    <v-app-bar-title>
      <RouterLink
        class="font-weight-bold text-decoration-none text-primary"
        to="/"
        >Bacala 📚</RouterLink
      >
    </v-app-bar-title>

    <v-toolbar-items>
      <Navbar :categories="data" />
      <v-divider inset vertical></v-divider>
      <v-btn variant="text">
        <RouterLink class="text-decoration-none" to="/about">About</RouterLink>
      </v-btn>
    </v-toolbar-items>

    <template v-slot:append>
      <v-btn icon="mdi-heart"></v-btn>
      <v-btn icon="mdi-magnify"></v-btn>
      <v-app-bar-nav-icon class="ms-2"></v-app-bar-nav-icon>
    </template>
  </v-app-bar>
</template>
