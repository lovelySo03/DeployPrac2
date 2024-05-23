<template>
  <div class="total">
    <header>
      <Nav></Nav>
    </header>
    <RouterView />
    <Footer class="footer"/>
  </div>
</template>

<script setup>
import { RouterView, useRouter } from 'vue-router';
import Nav from '@/components/SY/Nav.vue'
import Footer from '@/components/SY/Footer.vue'
</script>

<style scoped>
.total{
  background-color: white;
}
.footer {
  /* position: absolute;
  bottom: -200px; */
  position: relative;
  bottom: -150px;
  transform : translateY(100%);
}
</style>
