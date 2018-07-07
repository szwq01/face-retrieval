<template>
  <el-card  v-loading="loading" shadow="hover" style="margin: auto;text-align:center;max-height:200px;max-width:200px;cursor:pointer" :body-style="{ padding: '0px' }">
    <img @load="loading=false" v-if="photoName" :src="url" class="image">
    <div v-else>暂无图片</div>
  </el-card>
</template>
<script>
export default {
  props: {
    photoName: '',
    libraryName: ''
  },
  data() {
    return {
      loading: true
    }
  },
  computed: {
    url: function() {
      return `/api/photos/${this.libraryName}/${this.photoName}`
    }
  },
  watch: {
    photoName: function(oldVal, newVal) {
      this.loading = true
    }
  }
}
</script>
<style scoped>
.image {
  width: 100%;
  display: block;
}
</style>
