---
title: "GPU-S: A Tiny GPU Monitor for Windows AI Developers"
date: 2026-11-24T14:00:00-05:00
area: AI developer tools, GPU monitoring
summary: "A free, 195 KB GPU monitor for AI developers on Windows. The S stands for simple: no installation, no admin rights, and the same numbers as nvidia-smi."
image: media/projects/gpu-s/gpu-s-monitor.png
repo_url: https://github.com/gladcolor/GPU-S
tags:
- AI Developer Tools
- GPU Monitoring
- NVIDIA
- Windows
---
When I train models on my Windows workstation, I want to see what the GPU is doing. Most tools make that harder than it should be:

- **Task Manager shows 0% GPU** while PyTorch trains at full speed. Its default graphs leave out CUDA.
- **nvidia-smi shows "N/A"** for each process's memory on Windows, and it is a text tool, not a live graph.
- **GPU-Z and HWiNFO need admin rights.** On a university or company PC, I don't have them.

So I built **GPU-S**. The **S** stands for **simple**: one small file you double-click. It needs no installation and no admin rights, and it shows the GPU readings an AI developer cares about.

**[Download GPU-S.exe](https://github.com/gladcolor/GPU-S/releases/latest/download/GPU-S.exe)** (195 KB, Windows 10/11 x64). It is free and open source, with no ads and no tracking, and it sends nothing over the network.

## Everything on one page, Task Manager style

![The GPU-S Monitor tab: large graphs of GPU utilization and GPU memory, then four smaller graphs of temperature with the hot spot as a dashed line, CPU, system RAM and network, and a stats grid with power and fan RPM](media/projects/gpu-s/gpu-s-monitor.png)

The Monitor tab looks like Windows Task Manager, but the GPU is the main subject:

- **GPU utilization** includes CUDA, so it is the same number nvidia-smi reports.
- **GPU memory** shows exact MB used and free. The graph turns orange at 90% and red at 95%, before an out-of-memory error.
- **Temperature** shows the GPU core as a filled area and the **hot spot** as a dashed line. The hot spot is the hottest point on the chip, and throttling reacts to it.
- **CPU, system RAM and network** graphs sit next to the GPU. If GPU use is low while CPU use is high, the data loader is usually the bottleneck. If the network graph is busy, you may be waiting on a download or remote storage.
- The stats at the bottom show power, clocks and **fan speed in RPM**.

You can view the last minute, 10 minutes or hour. The **All GPUs** view puts every GPU in the machine side by side.

## Built for training runs

A few features come straight from problems I hit while training:

- **Which process is using my VRAM?** The Processes tab shows dedicated and shared GPU memory for each program. Windows hides this from nvidia-smi.
- **Silent slowdowns.** When VRAM fills up, the NVIDIA driver can quietly move data into system RAM, and training gets many times slower. GPU-S spots this and warns you, with the setting that turns it off.
- **Throttling.** A badge shows when the GPU is held back by its power limit or temperature.
- **Numbers for papers and job tuning.** Report → *Copy run summary* produces a Markdown table: average and maximum utilization, peak GPU memory, maximum temperature and hot spot, power, time throttled, CPU, RAM and network traffic.
- **Logging in nvidia-smi format.** Run `GPU-S.exe --log run.csv` from the command line. The CSV has the same columns as `nvidia-smi --query-gpu=... --format=csv`, so existing parsing scripts still work, and a run summary is saved next to it.

![The Processes tab: each program that uses the GPU, with its dedicated and shared GPU memory](media/projects/gpu-s/gpu-s-processes.png)

There is also a small always-on-top **mini window**, a tray icon with alerts for temperature and memory, and a **Details** tab with architecture, CUDA cores, PCIe link, Resizable BAR status, driver and CUDA version.

![The Details tab: GPU name, architecture, CUDA cores, BIOS version, memory size and bus width, Resizable BAR status, and PCIe link](media/projects/gpu-s/gpu-s-details.png)

The interface is in eight languages: English, 简体中文, 繁體中文, 日本語, 한국어, Español, Français and Deutsch. It follows your Windows language automatically.

## Same numbers as nvidia-smi

A monitor is only useful if you trust it. I logged GPU-S and nvidia-smi side by side. Utilization, temperature, power, clocks, fan speed and power state matched.

One reading did not match at first: GPU-S reported about 300 MB more memory in use than nvidia-smi. The old NVIDIA call counts memory the driver reserves for itself as "used". GPU-S now uses the same newer call as nvidia-smi, and the used memory matches to the MB.

## Small on purpose

A monitor should not slow down the job it watches:

- **One 195 KB file.** For comparison, the GPU-Z download is about 12 MB.
- **About 10 MB of RAM** in Task Manager and about 1% of one CPU core while running.
- **Nothing to install.** GPU-S is built with the C# compiler that ships with Windows, and it runs on the .NET Framework that every Windows 10/11 PC already has.

Getting the memory down took some measuring. I checked what each part costs: the .NET runtime, NVIDIA's own library, and the Windows performance counters. Two parts were wasting memory, so I removed them. Checking which DirectX, Vulkan and OpenCL versions the GPU supports, and reading the CUDA version, loads large driver files. GPU-S now does that once, in a helper process that exits a few seconds later. I also ran 7,200 rounds of sampling and drawing to confirm there is no memory leak.

## Limits

- **Per-process GPU % for CUDA is not available on Windows.** In the normal Windows driver mode, Windows does not track CUDA compute time per process. No tool can show it, including `nvidia-smi pmon`. Per-process memory is exact.
- **The hot-spot and memory-junction temperatures** come from an undocumented NVIDIA driver interface, the same one GPU-Z and HWiNFO use. If a future driver changes it, GPU-S hides those two readings and keeps everything else.
- GPU-S works best with NVIDIA GPUs. AMD and Intel GPUs get basic monitoring through Windows performance counters.

## Try it

1. Download **[GPU-S.exe](https://github.com/gladcolor/GPU-S/releases/latest/download/GPU-S.exe)**.
2. Double-click it.

If Windows SmartScreen warns about an unknown publisher, click **More info → Run anyway**. This doesn't need admin rights either. The source code is on [GitHub](https://github.com/gladcolor/GPU-S) under the MIT license. Bug reports and suggestions are welcome.

**Links:** [Download GPU-S.exe](https://github.com/gladcolor/GPU-S/releases/latest/download/GPU-S.exe) · [Source on GitHub](https://github.com/gladcolor/GPU-S) · [All releases](https://github.com/gladcolor/GPU-S/releases)
