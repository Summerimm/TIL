<template>
  <div>
    <li @click="updateMovie" :class="{ 'isCompleted': movie.isCompleted }">{{ movie.title }}</li>
  </div>
</template>

<script>
export default {
  name: 'WatchListItem',
  props: {
    movie: Object,
  },
  methods: {
    updateMovie() {
      this.$store.dispatch('updateMovie', this.movie)
    }
  }
}
</script>

<style>
.isCompleted {
  text-decoration: line-through;
}
</style>