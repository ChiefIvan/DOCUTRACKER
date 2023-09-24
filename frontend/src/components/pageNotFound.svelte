<script>
  import { onMount } from "svelte";
  import pageError from "../lib/pagenotfound_banner.png";

  onMount(() => {
    document.title = "404 | Page not found";
  });
</script>

<main>
  <div>
    <img src={pageError} alt="page error banner" />
  </div>
  <h1>Opps!</h1>
  <h3>Error 404 | Page not found</h3>
  <article>
    <p>The page you requested could not be found.</p>
    <p>We're working on it ^_^.</p>
  </article>
</main>

<style>
  main {
    position: fixed;
    height: 100%;
    width: 100%;

    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;

    & div {
      & img {
        max-width: 25rem;
      }
    }

    & h1 {
      font-family: Arial, Helvetica, sans-serif;
      font-weight: bolder;
      font-size: 5rem;
    }

    & h3 {
      color: crimson;
      margin: 1rem;
      font-size: 1.5rem;
    }

    & article {
      margin: 1.5rem 0;
      text-align: center;
    }
  }
</style>
