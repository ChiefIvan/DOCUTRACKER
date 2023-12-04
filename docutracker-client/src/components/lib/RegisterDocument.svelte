<script lang="ts">
  import { dark, handleFetch, type RequestAPI } from "../../store";
  import { v4 as uuidv4 } from "uuid";
  import { fade } from "svelte/transition";

  import Input from "../shared/Input.svelte";
  import QrCode from "svelte-qrcode";
  import Button from "../shared/Button.svelte";

  let placeholderHovered = false;
  let qrCodeElement: any;

  export let fullname: {
    firstName: string;
    middleName: string;
    lastName: string;
  };

  const date = new Date().toLocaleDateString("en-US", {
    weekday: "long",
    year: "numeric",
    month: "long",
    day: "numeric",
  });

  let value: string;
  const handleGenerate = () => {
    value = uuidv4();
  };

  const handleDownload = () => {
    let imgElement = qrCodeElement.querySelector("img.qrcode");
    let base64Image = imgElement.src;

    const downloadLink = document.createElement("a");
    downloadLink.href = base64Image;
    downloadLink.download = "Image.png";
    downloadLink.click();
  };

  const handleSubmit = () => {};
</script>

<div class="register-document-wrapper">
  <form class="register-document-form" on:submit={handleSubmit}>
    <div class="credential-wrapper">
      <span class="date"
        >Author: {fullname.firstName}
        {fullname.middleName}
        {fullname.lastName}</span
      >

      <Input
        inputName="Document Name"
        inputType="Text"
        overlap={true}
        on:input={() => {}}
      ></Input>
      <textarea placeholder="Description" required></textarea>
      <div class="button-wrapper">
        <Button>Submit</Button>
      </div>
    </div>
    <div class="code-wrapper">
      <span class="date">{date}</span>
      <!-- svelte-ignore missing-declaration -->
      <!-- svelte-ignore a11y-click-events-have-key-events -->
      <!-- svelte-ignore a11y-no-static-element-interactions -->
      <div
        class="code-placeholder"
        bind:this={qrCodeElement}
        on:click|once={handleGenerate}
        on:mouseenter={() => {
          placeholderHovered = true;
        }}
        on:mouseleave={() => {
          placeholderHovered = false;
        }}
      >
        {#if value && value.length}
          <QrCode {value}></QrCode>
          {#if value && value.length && placeholderHovered}
            <div transition:fade class="code-overlap" on:click={handleDownload}>
              <span class="download-qr">Download Image</span>
            </div>
          {/if}
        {:else}
          <span class="qr-label">Generate QR Code</span>
        {/if}
      </div>
    </div>
  </form>
</div>

<style>
  span {
    font-size: 1rem;
    font-weight: 700;
    color: var(--scroll-color);
  }

  div.register-document-wrapper {
    padding: 2rem;
    height: 100%;
    /* background-color: gray; */

    & form {
      display: flex;
      justify-content: center;
      column-gap: 10rem;
      height: 100%;

      & div.credential-wrapper {
        width: 100%;

        & textarea {
          outline: none;
          transition: 300ms;
          background-color: transparent;
          border-radius: 0.5rem;
          padding: 0.5rem;
          width: 100%;
          height: 79%;
          min-width: 20%;
          min-height: 20%;
          border: 1px solid var(--header-color);
          color: var(--scroll-color);
        }

        & textarea:hover {
          border-color: var(--border-hover-color);
        }

        & textarea:focus {
          border-color: var(--border-active-color);
        }

        & div.button-wrapper {
          display: inline-block;
          width: 10rem;
          text-align: end;
          margin-top: 1rem;
        }
      }

      & div.code-wrapper {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: space-between;

        & div.code-placeholder {
          overflow: hidden;
          position: relative;
          border-radius: 1rem;
          transition: all ease-in-out 300ms;
          background-color: var(--main-col-1);
          width: 15rem;
          height: 15rem;
          display: flex;
          align-items: center;
          justify-content: center;
          cursor: pointer;

          & span.qr-label {
            transition: color ease-in-out 300ms;
            color: var(--background);
            margin: auto;
            font-weight: normal;
            font-size: 0.9rem;
          }

          & img.qrcode {
            border-radius: 0.5rem;
          }

          & div.code-overlap {
            position: absolute;
            transition: all ease-in-out 300ms;
            inset: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            z-index: 1;

            & span.download-qr {
              color: var(--background);
            }
          }

          & div.code-overlap:hover {
            background-color: rgba(84, 84, 84, 0.9);
          }
        }

        & div.code-placeholder:hover {
          background-color: var(--main-col-2);
          box-shadow: 1px 2px 3px var(--main-col-2);
        }

        & div.code-placeholder:hover span.qr-label {
          color: var(--scroll-color);
        }
      }
    }
  }
</style>
