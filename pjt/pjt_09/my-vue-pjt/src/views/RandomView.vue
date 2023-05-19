<template>
  <div>
    <button type="button" class="btn btn-success mb-2" style="width: 500px" @click="randomMovie">PICK</button>
    <div v-if="movie">
      <p><img :src="posterUrl" alt="Movie poster"></p>
      <p style="font-weight: bold">{{ movie.title }}</p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'RandomView',
  created() {
    this.$store.dispatch('getMovies')
  },
  methods: {
    randomMovie() {
      this.$store.dispatch('getMovies')
    }
  },
  computed: {
    movie() {
      return this.$store.state.randomMovie
    },
    posterUrl() {
      const baseUrl = 'https://image.tmdb.org/t/p/w500'
      return `${baseUrl}${this.movie.poster_path}`
    }
  }
}
</script>

<style>

</style>