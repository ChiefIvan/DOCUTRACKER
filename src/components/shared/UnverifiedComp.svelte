<script>
  import errorBanner from "./../../assets/pagenotfound_banner.png";
</script>

<div class="main">
  <div class="main-container">
    <img src={errorBanner} alt="page error banner" />
    <h1>Opps!</h1>
    <h3>Please Verify Your Account First!</h3>
    <section>
      <p>You need to be a verfied user of Docutracker!</p>
      <p>To use its Features.</p>
    </section>
  </div>
</div>

<style>
  div.main {
    display: flex;
    align-items: center;
    justify-content: center;
    height: 100%;

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
