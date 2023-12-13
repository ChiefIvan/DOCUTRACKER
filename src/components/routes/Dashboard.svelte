<script lang="ts">
  import { activeDocument, documentTimeZone, type Document } from "../../store";

  import moment from "moment";
  import CheckAuthenticity from "../shared/CheckAuthenticity.svelte";
  import MediaQuery from "../shared/MediaQuery.svelte";
  import DocumentAvail from "../lib/DocumentAvail.svelte";
  import UnprocessedIcon from "../icons/UnprocessedIcon.svelte";
  import ApprovedIcon from "../icons/ApprovedIcon.svelte";

  export let authToken = "";
  let days = 0;
  let hours = 0;
  let minutes = 0;
  let seconds = 0;
  let timer: string | number | NodeJS.Timeout | undefined;

  export let routes: Document = {
    codeData: "",
    documentName: "",
    documentDescription: "",
    documentRegDate: "",
    documentPath: [{ name: "", approved: false }],
  };

  $: timer = setInterval(() => {
    let currentTime = moment();
    let eventTime = moment($documentTimeZone, "ddd, DD MMM YYYY HH:mm:ss z");

    if (currentTime.isAfter(eventTime)) {
      let duration = moment.duration(currentTime.diff(eventTime));

      days = duration.days();
      hours = duration.hours();
      minutes = duration.minutes();
      seconds = duration.seconds();
    } else {
      console.warn("Event hasn't occurred yet");
      return;
    }
  }, 1000);
</script>

<svelte:head>
  <title>DOCUTRACKER | Dashboard</title>
</svelte:head>

<CheckAuthenticity {authToken} on:user></CheckAuthenticity>
<main>
  <MediaQuery query="(max-width: 500px) " let:matches>
    {#if matches}
      <DocumentAvail document={routes} inner={true}></DocumentAvail>
    {/if}
  </MediaQuery>

  <div class="track-info">
    <div class="info" class:not-selected={!$activeDocument.length}>
      {#if $activeDocument.length}
        <div class="doc-lifecycle-wrapper">
          <div class="counter">
            {#if routes && routes.documentRegDate && routes.documentRegDate.length}
              {routes.documentRegDate}
            {:else}
              <span class="timer-container"> {days}d {hours}h </span><br />
              <span class="timer-container sec"> {minutes}m {seconds}s </span>
            {/if}
          </div>
          <span class="counter-label"> Document Lifecycle </span>
        </div>
        <ul class="doc-route-wrapper">
          {#if routes.length}
            {#each routes as route (route)}
              {#if route.documentName === $activeDocument}
                {#if route.codeData && route.codeData.length}
                  {#each route.documentPath as path}
                    <li class="route">
                      <div class="wrapper">
                        <span class="route-name">
                          {path.name}
                        </span>
                        <span>
                          {#if !path.approved}
                            <ApprovedIcon></ApprovedIcon>
                            Approved
                          {:else}
                            <UnprocessedIcon></UnprocessedIcon>
                            Processing...
                          {/if}
                        </span>
                      </div>
                    </li>
                  {/each}
                {/if}
              {/if}
            {/each}
          {/if}
        </ul>
      {:else}
        <span class="not-selected">Please select a Document first</span>
      {/if}
    </div>
  </div>
</main>

<style>
  main {
    & div.track-info {
      display: flex;
      justify-content: center;
      padding: 4rem 0;
      /* background-color: var(--main-col-7); */
      background-color: var(--header-color);

      margin: auto;

      & div.info {
        display: flex;
        width: 80rem;
        overflow: hidden;
        flex-wrap: nowrap;
        height: 25rem;

        & div.doc-lifecycle-wrapper {
          display: flex;
          align-items: center;
          justify-content: center;
          flex-direction: column;
          min-width: 20rem;

          & div.counter {
            -webkit-mask: linear-gradient(
              90deg,
              transparent,
              white 20%,
              white 80%,
              transparent
            );
            text-align: center;
            padding: 1rem;
            width: 90%;

            border-radius: 1rem;
            background-color: var(--main-col-1);

            & span.timer-container {
              font-size: 3rem;
              font-weight: 700;
            }

            & span.timer-container.sec {
              font-size: 1rem;
              font-weight: 700;
            }
          }

          & span.counter-label {
            margin-top: 1rem;
            color: var(--background);
            font-size: 1rem;
          }
        }
      }

      & div.not-selected {
        justify-content: center;
        align-items: center;
      }

      & ul.doc-route-wrapper {
        height: 100%;
        -webkit-mask: linear-gradient(
          90deg,
          transparent,
          white 20%,
          white 80%,
          transparent
        );
        padding: 2rem;
        padding-left: 7rem;
        overflow-y: auto;
        overscroll-behavior-inline: contain;
        white-space: nowrap;

        & li.route {
          color: var(--scroll-color);
          width: 10rem;
          font-weight: 700;
          display: inline-block;

          & div.wrapper {
            display: flex;
            align-items: center;
            justify-content: center;
            flex-direction: column;
            text-align: center;

            & span.route-name {
              font-weight: 700;
              margin-bottom: 10rem;
            }
          }
        }
      }

      & span.not-selected {
        font-size: 2rem;
        font-weight: 700;
        word-spacing: 0.2rem;
        letter-spacing: -0.08rem;
        color: var(--scroll-color);
      }

      & ul.doc-route-wrapper::-webkit-scrollbar {
        width: 0.5rem;
        height: 0.5rem;
      }

      & ul.doc-route-wrapper::-webkit-scrollbar-track {
        background: var(--main-col-6);
      }

      & ul.doc-route-wrapper::-webkit-scrollbar-thumb {
        background: var(--main-col-3);
      }

      & ul.doc-route-wrapper::-webkit-scrollbar-thumb:hover {
        background: var(--scroll-color);
      }
    }
  }

  @media (max-width: 1400px) {
    main div.track-info div.info {
      width: 70rem;
    }
  }

  @media (max-width: 1250px) {
    main div.track-info div.info {
      width: 60rem;
    }
  }

  @media (max-width: 1100px) {
    main div.info ul.doc-route-wrapper li.route div.wrapper span.route-name {
      margin-bottom: 1.9rem;
    }

    main div.track-info div.info {
      flex-direction: column;
      width: 40rem;
    }
  }

  @media (max-width: 800px) {
    main div.track-info div.info {
      width: 30rem;
    }
  }

  @media (max-width: 650px) {
    main div.track-info div.info {
      width: 25rem;
    }
  }
</style>
