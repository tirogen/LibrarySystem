import Vue from 'vue'
import Router from 'vue-router'
import VueDemo from '@/components/VueDemo'
import Messages from '@/components/Messages'
import Librarian from '@/components/Librarian'
import Student from '@/components/student'
//Routes import below//
import studentRoutes from './components/student/routes'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: VueDemo
    },
    {
      path: '/messages',
      name: 'messages',
      component: Messages
    },
    {
      path: '/librarian',
      name: 'librarian',
      component: Librarian
    },
    studentRoutes,
  ]
})
