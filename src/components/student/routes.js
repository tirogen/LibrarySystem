import StudentLayout from './index.vue'
import Dashboard from './Dashboard/Dashboard.vue'
import ReserveRoom from './ReserveRoom/index.vue'

export const studentRoutes = {
  path: '/student',
  component: StudentLayout,
  children: [
    {
      path: '',
      name: 'student',
      component: Dashboard
    },
    {
      path: 'reserve-room',
      component: ReserveRoom
    }
  ]
}

export default studentRoutes