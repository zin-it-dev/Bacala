<script setup lang="ts">
import type { Category } from "@/services/category.service";

defineProps<{
  categories: Category[];
}>();
</script>

<template>
  <v-menu open-on-hover>
    <template v-slot:activator="{ props }">
      <v-btn color="primary" v-bind="props">Categories</v-btn>
    </template>

    <v-list>
      <v-list-item v-for="cat in categories" :key="cat.id">
        <v-list-item-title>{{ cat.name }}</v-list-item-title>
      </v-list-item>
    </v-list>
  </v-menu>
</template>
