export type Seg = { text: string; token?: string };

export function buildSegments(resultText: string, table: Record<string, string>): Seg[] {
	const entries = Object.entries(table)
		.map(([token, orig]) => ({ token, orig: orig.trim() }))
		.sort((a, b) => b.orig.length - a.orig.length);

	let segs: Seg[] = [{ text: resultText }];

	for (const { token, orig } of entries) {
		const next: Seg[] = [];
		for (const seg of segs) {
			if (seg.token || !seg.text.includes(orig)) {
				next.push(seg);
				continue;
			}
			const parts = seg.text.split(orig);
			for (let i = 0; i < parts.length; i++) {
				if (parts[i]) next.push({ text: parts[i] });
				if (i < parts.length - 1) next.push({ text: orig, token });
			}
		}
		segs = next;
	}
	return segs;
}
