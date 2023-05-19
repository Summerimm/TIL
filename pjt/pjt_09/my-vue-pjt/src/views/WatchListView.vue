<template>
  <div>
    <WatchListForm />
    <WatchListItem v-for="(movie, index) in MovieList" :key="index" :movie=movie />
  </div>
</template>

<script>
import WatchListForm from '@/components/WatchListForm'
import WatchListItem from '@/components/WatchListItem'

export default {
  name: 'WatchListView',
  components: {
    WatchListForm,
    WatchListItem,
  },
  computed: {
    MovieList() {
      return this.$store.state.movielist
    }
  },
  created() {
      this.$store.dispatch('loadMovies')
  }
}
</script>

<style>

</style>