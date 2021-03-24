function init() {
  document.body.classList.remove("loading");
  // var rev1 = new RevealFx(document.querySelector("#rev-1"), {
  //   revealSettings: {
  //     bgcolor: "#000000",
  //     onCover: function (contentEl, revealerEl) {
  //       contentEl.style.opacity = -1;
  //     },
  //   },
  // });
  // rev1.reveal();
  $(".modal_close_x").on("click", function () {
    $("#video1").attr("src", "");
  });
  $(".modal_close_x2").on("click", function () {
    $("#video1").attr("src", "");
  });
}

setTimeout(() => {
  if (!!document.querySelector("#rev-1")) {
    init();
  }
}, 500);
