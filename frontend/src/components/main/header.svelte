<script>
  // @ts-nocheck

  import {
    fetchData,
    winEvent,
    dark,
    openProfile,
    expand,
    openVerSec,
  } from "../../stores";
  import { fade } from "svelte/transition";

  import WinEvents from "../winEvents/winEvents.svelte";
  import UserIcon from "../assets/userIcon.svelte";
  import Mode from "./mode.svelte";
  import myImg from "../../lib/me.jpg";
  import Button from "../entries/button.svelte";
  import UserFullVerification from "./userFullVerification.svelte";

  let userName, verified;

  $: {
    userName = $fetchData.user_name;
    verified = $fetchData.fully_ver_val;
  }

  const handleUserProfiles = () => {
    $expand = false;
    $openProfile = !$openProfile;
  };

  const openVerificationSection = () => {
    $openVerSec = true;
  };
</script>

<WinEvents />
<div class="header-wrapper" class:dark={$dark} class:has-scrolled={$winEvent}>
  <h1 class:dark={$dark}>
    Hello, {userName !== undefined ? userName : "Anonymous"}
  </h1>
  <div class="r-side-wrapper">
    <Mode />
    <UserIcon on:click={handleUserProfiles} />
  </div>
</div>

{#if $openProfile}
  <div
    transition:fade={{ duration: 150, delay: 0 }}
    class="profiles"
    class:not-verified-wrapper={!verified}
  >
    {#if verified}
      <section class="upper-wrapper">
        <!-- svelte-ignore a11y-img-redundant-alt -->
        <img src={myImg} alt="User Profile Picture" />
        <p>dorsu.dawangivan@gmail.com</p>
      </section>
      <section class="lower-wrapper">Hello</section>
    {:else}
      <Button
        on:click={openVerificationSection}
        btnName={"Full Verfication"}
        btnLoginSize={true}
        btnTitle={"Get a full verification"}
      />
    {/if}
  </div>
{/if}

{#if $openVerSec}
  <UserFullVerification />
{/if}

<style>
  div.header-wrapper {
    position: sticky;
    top: 0;
    z-index: 1;

    background-color: var(--main-col-6);
    padding: 0 calc(var(--size-1) * 1.1);
    height: var(--size-3);
    transition: all ease-in-out var(--dur2);

    display: flex;
    justify-content: space-between;
    align-items: center;

    & h1 {
      color: var(--main-col-3);
      font-weight: 700;
    }

    & h1.dark {
      color: var(--bg);
    }

    & div.r-side-wrapper {
      display: flex;
      justify-content: center;
      align-items: center;
      column-gap: 1rem;
    }
  }

  /* div.has-scrolled {
    box-shadow: 2px 0px 5px var(--main-col-1);
  } */

  div.dark {
    background-color: var(--dark-main-col-2);
    box-shadow: none;
  }

  div.profiles {
    position: fixed;
    top: 3.5rem;
    right: var(--size-6);

    background-color: var(--bg);
    border-radius: var(--size-1);
    overflow: hidden;
    box-shadow: 5px 5px 25px var(--main-col-2);

    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
    row-gap: var(--size-1);
    padding: var(--size-3);

    & section.upper-wrapper {
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      row-gap: var(--size-6);
      /* background-color: var(--dark-main-col-2); */
      border-radius: calc(var(--size-1) * 0.5);

      & img {
        max-width: var(--size-4);
        border-radius: 50%;
      }

      & p {
        border-radius: calc(var(--size-1) * 0.5);
      }
    }
  }

  div.not-verified-wrapper {
    padding: var(--size-6);
    width: calc(var(--size-2) * 2);
    border-radius: var(--size-6);
  }
</style>
