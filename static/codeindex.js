/**
 * Created by jensen on 21/10/15.
 */
    function changeArea(obj){
        var btn = $(obj).parents("#cell").children("#comment")
        if(btn.hasClass("expand-enter")){
            btn.removeClass("expand-enter").addClass("expand-transition")
            $(obj).text("隱藏評論")
        }else{
            btn.addClass("expand-enter").removeClass("expand-transition")
          $(obj).text("顯示評論")
        }
    }
var homework = new Vue({
  el: '#homework',
  data: {
    showadd:false,
    title: 'todos',
  },
    ready: function() {
        if(document.getElementById('errormsg')){
          this.showadd=true
        }
    },
  methods:{
    showaddform:function(e){
      this.showadd=true
      if(document.getElementById('errormsg')){
        document.getElementById('errormsg').remove();
     }
    },
    hiddenform:function(e){
      this.showadd=false
    },
    fileup:function(e){
      document.getElementById('filebtn').innerHTML = document.getElementById('fileup').value
    }
  }
});
