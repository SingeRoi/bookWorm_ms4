describe("js fuction tests", function() {
  describe("test update", function () {

    it("tracks if update function was called at all", function() {
      spyOn(window, 'update');
      window.update();
      expect(window.update.calls.any()).toEqual(true);
      window.update.calls.reset();
      expect(window.update.calls.any()).toEqual(false);
      });
  });

  describe("test update", function () {

      it("tracks if update function was called at all", function() {
        spyOn(window, 'update');
        window.update();
        expect(window.update.calls.any()).toEqual(true);
        window.update.calls.reset();
        expect(window.update.calls.any()).toEqual(false);
        });
    });
});