<template>
  <div>
    <input 
      type="text" 
      v-model="title" 
      @keyup.enter="createTodo"
    >
    <button @click="createTodo">+</button>
  </div>
</template>

<script>
import axios from'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'CreateTodo',
  data: function () {
    return {
      title: null,
      is_completed: null,
    }
  },
  methods: {
    createTodo() {
      const title = this.title
      const is_completed = this.is_completed
      if (!title) {
        alert('제목을 입력해주세요')
        return
      } 
      axios({
        method: 'post',
        url: `${API_URL}/todos/`,
        data: { title, is_completed },
      })
        .then((res) => {
          console.log(res)
        })
        .catch((err) => {
          console.log(err);
        })
    },
  },
}
</script>