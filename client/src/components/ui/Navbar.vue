<template>
  <ul>
    <li v-for="cat in categories" :key="cat.id">
      {{ cat.name }}
    </li>
  </ul>
</template>

<script setup lang="ts">
import type { Category } from "@/services/category.service";

defineProps<{
  categories: Category[];
}>();
</script>
