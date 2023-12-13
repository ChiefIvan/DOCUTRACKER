<script>
  import { tooltip } from "../shared/Tooltip";
  import { Link, navigate } from "svelte-routing";

  import ArrowIcon from "../icons/ArrowIcon.svelte";
  import errorBanner from "./../../assets/pagenotfound_banner.png";
  import Footer from "../lib/Footer.svelte";

  const tooltipContent = "Go Back to Overview";

  const handleNavigate = () => {
    navigate("/");
  };
</script>

<svelte:head>
  <title>404 | Page not found</title>
</svelte:head>

<header class="header">
  <div class="header-container">
    <div
      class="arrow-container"
      use:tooltip={{
        content: tooltipContent,
        animation: "perspective-subtle",
        theme: "tooltip",
      }}
    >
      <ArrowIcon arrowState={true} dark={true} on:click={handleNavigate} />
    </div>
    <Link to="/terms">
      <span>Terms</span>
    </Link>
  </div>
</header>

<main>
  <div class="main-container">
    <img src={errorBanner} alt="page error banner" />
    <h1>Opps!</h1>
    <h3>Error 404 | Page not found</h3>
    <section>
      <p>The page you requested could not be found.</p>
      <p>We're working on it ^_^.</p>
    </section>
  </div>
</main>
<Footer />

<style>
  header.header {
    position: fixed;
    top: 0;
    width: 100%;
    background-color: var(--header-color);
    z-index: 3;

    & div.header-container {
      padding: 0.5rem 1rem;
      display: flex;
      justify-content: space-between;
      align-items: center;

      & div.arrow-container {
        display: flex;
        align-items: center;
      }

      & span {
        text-decoration: none;
        color: var(--background);
        transition: all ease-in-out 200ms;
      }

      & span:hover {
        opacity: 0.6;
        text-decoration: underline;
      }
    }
  }

  main {
    display: flex;
    align-items: center;
    justify-content: center;
    height: 90vh;

    & div.main-container {
      text-align: center;
      min-width: 15rem;
      padding: 1rem;

      & img {
        width: -webkit-fill-available;
      }

      & h1 {
        font-weight: bolder;
        font-size: 2.5rem;
        color: var(--main-col-3);
      }

      & h3 {
        color: crimson;
        margin: 1rem;
        font-size: 1.5rem;
      }

      & section {
        margin: 1.5rem 0;
        text-align: center;
        color: var(--main-col-3);
      }
    }
  }
</style>
