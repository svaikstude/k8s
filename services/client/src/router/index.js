import Vue from 'vue';
import Router from 'vue-router';
import Ping from '@/components/Ping';
import Tables from '@/components/Tables';

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Tables',
      component: Tables,
    },
    {
      path: '/ping',
      name: 'Ping',
      component: Ping,
    },
  ],
  mode: 'hash',
});
