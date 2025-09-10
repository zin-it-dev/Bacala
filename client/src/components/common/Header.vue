<template>
  <header>
    <nav>
      <RouterLink to="/">Home</RouterLink>
      <RouterLink to="/about">About</RouterLink>
    </nav>
    <Navbar :categories="data" />
  </header>
</template>

<script setup lang="ts">
import { onMounted, ref } from "vue";

import { getCategories } from "@/services/category.service";

const data = ref();

onMounted(async () => {
  try {
    data.value = await getCategories();
  } catch (error) {
    console.error(error);
  }
});
</script>
