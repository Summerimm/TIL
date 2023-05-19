// store/index.js

actions: {
  fetchTodoList: async function ({ commit }) {
    const requestUrl = 'http://localhost:8000/api/v1/todos/'

    const response = await axios.get(requestUrl)
    commit('TODO_LIST_SUCCESS', response)
  },
}