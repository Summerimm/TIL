<template>
  <div class="card" style="width: 18rem; padding: 0px;">
    <img :src="posterUrl" class="card-img-top" alt="Movie poster" style="object-fit: cover; height: 420px;">
    <div class="card-body">
      <h5 class="card-title" style="font-weight: bold;">{{ movie.title }}</h5>
      <p class="card-text">{{ movie.overview }}</p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'MovieCard',
  props: {
    movie: Object,
  },
  computed: {
    posterUrl() {
      const baseUrl = 'https://image.tmdb.org/t/p/w200'
      return `${baseUrl}${this.movie.poster_path}`
    }
  }
}
</script>

<style>
.card {
  margin: 0 10px 20px;
}

.card-text {
  height: 100px; 
  overflow-y: hidden; 
  overflow-x: hidden; 
  text-overflow: ellipsis; 
  white-space: pre-wrap; 
  display: -webkit-box; 
  -webkit-box-orient: vertical; 
  -webkit-line-clamp: 4;
}
</style>