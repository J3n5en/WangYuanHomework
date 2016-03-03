/**
 * Created by jensen on 21/10/15.
 */
var test = new Vue({
  el: '#homework',
  data: {
    showadd:false,
    title: 'todos',
    works:null,
    work:{
      isShow:false
    }
    //showcommit:false,
  },
    //ready: function() {
    //  this.getwork();
    //  this.cell=true;
    //
    //
    //},
  methods:{
    //getwork:function(e) {
    //  var xhr = new XMLHttpRequest()
    //  var self = this
    //  xhr.open('GET', '/getnewwork')
    //  xhr.onload = function () {
    //    self.works = JSON.parse(xhr.responseText)
    //  }
    //  xhr.send()
    //},
    //togglecomment:function(work){
    //  if(work.isShow != false){
    //    work.isShow = false
    //    work.btn = "隱藏詳情"
    //  }else{
    //    work.isShow = true
    //    work.btn = "顯示詳情"
    //  }
    //},
  }
});
