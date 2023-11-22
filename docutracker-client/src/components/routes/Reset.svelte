<script lang="ts">
  import {
    address,
    handleFetch,
    showMessage,
    type ResponseData,
  } from "../../store";
  import { Timer } from "../shared/Timer";
  import { Link, navigate } from "svelte-routing";

  import resetBanner from "./../../assets/forgot-password-banner.png";
  import logoElegant from "./../../assets/transparent-favicon-elegant.png";
  import Input from "../shared/Input.svelte";
  import Button from "../shared/Button.svelte";
  import MediaQuery from "../shared/MediaQuery.svelte";
  import BarLoader from "../shared/BarLoader.svelte";

  let emailInput = false;
  let bindForm: HTMLFormElement;
  let email: string;

  const timer = new Timer();
  timer.checkTimer(120_000, "fp");

  const handleInput = (event: Event) => {
    const target = event.target as HTMLInputElement;
    email = target.value;
  };

  const resendMethod = "POST";
  const resendAddress = `${address}/reset`;

  $: disabled = $timer <= 0;

  $: resendRequest = {
    method: resendMethod,
    address: resendAddress,
    credentials: {
      email: email,
      btnDisabled: !disabled,
    },
  };

  let isRequest = false;
  let timeOutID: number | undefined;

  const handleSubmit = async () => {
    isRequest = true;
    clearTimeout(timeOutID);

    try {
      const response: ResponseData = await handleFetch(resendRequest);

      bindForm.reset();
      (document.activeElement as HTMLElement).blur();
      emailInput = false;

      $showMessage = response;
      if (response.error) {
        isRequest = false;
        return;
      }

      if (response.success) {
        isRequest = false;
        timer.startTimer(120, "fp");
        navigate("/auth/login");

        timeOutID = setTimeout(() => {
          alert("If you can't see your Email, try checking out Spam Messages!");
        }, 1000);
      }
    } catch (error) {
      isRequest = false;
      console.error(error);
    }
  };
</script>

{#if isRequest}
  <BarLoader />
{/if}

<main>
  <MediaQuery query="(min-width: 700px)" let:matches>
    {#if matches}
      <img
        class="reset-banner"
        src={resetBanner}
        alt="Forgot Password Banner"
      />
    {/if}
  </MediaQuery>
  <div class="form-container">
    <MediaQuery query="(max-width: 700px)" let:matches>
      {#if matches}
        <img
          class="favicon-elegant"
          src={logoElegant}
          alt="Docutracker's Logo"
        />
      {/if}
    </MediaQuery>
    <div class="title-container">
      <h1>Forgot Password?</h1>
      <p class="warning">
        Please keep in mind that you only have 1 attemp to change your password
        every 7 days!
      </p>
    </div>
    <form
      class="form"
      bind:this={bindForm}
      on:submit|preventDefault={handleSubmit}
    >
      <Input
        inputName="Your Existing Email"
        on:input={handleInput}
        inputType="email"
        on:input={handleInput}
        bind:focusedInput={emailInput}
      />
      <Button hoverized={true} disabled={!disabled}
        >{!disabled ? `Resend again in ${$timer}s` : "Forgot Password"}</Button
      >
    </form>
    <p class="link">
      Go back to
      <Link to="/auth/login"><span>Login</span></Link>
    </p>
  </div>
</main>

<style>
  main {
    display: flex;
    align-items: center;
    justify-content: center;
    column-gap: 1rem;
    height: 90vh;
    color: var(--scroll-color);

    & img.reset-banner {
      max-width: 15rem;
    }

    & div.form-container {
      max-width: 25rem;
      width: 100%;
      margin: 0 2rem;

      & img.favicon-elegant {
        max-width: 5rem;
      }

      & div.title-container {
        margin-bottom: 2.5rem;

        & h1 {
          font-size: 2.5rem;
          font-weight: bold;
          letter-spacing: -0.12rem;
          color: var(--main-col-3);
        }

        & p.warning {
          color: var(--forground-color);
        }
      }
    }

    & p.link {
      margin-top: 1rem;

      & span {
        text-decoration: none;
        color: var(--border-hover-color);
        transition: all ease-in-out 200ms;
      }

      & span:hover {
        opacity: 0.6;
        text-decoration: underline;
      }
    }
  }

  @media (max-height: 600px) {
    main {
      margin: 5rem 0;
      text-align: center;
    }

    main img.reset-banner {
      display: none;
    }
  }

  @media (max-width: 700px) {
    main {
      text-align: center;
    }
  }
</style>
