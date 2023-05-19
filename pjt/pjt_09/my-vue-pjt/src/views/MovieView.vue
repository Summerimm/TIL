<template>
  <div class="container">
    <div class="row">
      <MovieCard
      v-for="movie in movies" :key="movie.index" :movie="movie"
      />
    </div>
  </div>
</template>

<script>
import MovieCard from '@/components/MovieCard'

export default {
  name: 'MovieView',
  components: {
    MovieCard
  },
  computed: {
    movies() {
      return this.$store.state.movies
    }
  },
  created() {
    this.getMovies()
  },
  methods: {
    getMovies() {
      this.$store.dispatch('getMovies')
    }
  }
}
</script>

<style>

</style>