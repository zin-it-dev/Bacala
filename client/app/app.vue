<script setup lang="ts">
const config = useRuntimeConfig()
const baseUrl = config.public.apiBase
const { data } = await useFetch(`${baseUrl}/users/`)
console.log(data)
</script>

<template>
  <NuxtLayout>
    <NuxtRouteAnnouncer />
    <p>{{ data }}</p>
  </NuxtLayout>
</template>
