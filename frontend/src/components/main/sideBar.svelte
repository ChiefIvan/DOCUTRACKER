<section>
  <nav>Hello Sidebar</nav>
</section>

<style>
  section {
    position: sticky;
    top: 0;
    left: 0;
    z-index: 2;

    display: flex;
    justify-content: center;
    align-items: center;

    min-width: 15rem;
    height: 100vh;
    background-color: #333;
    color: white;

    & nav {
      width: calc(15rem * 0.9);
      height: calc(100vh * 0.97);
    }
  }
</style>
