import com.fasterxml.jackson.annotation.*;

import java.util.HashMap;
import java.util.List;
import java.util.Map;


@JsonInclude(JsonInclude.Include.NON_NULL)
@JsonPropertyOrder({
        "start",
        "end",
        "text",
        "relevance",
        "keywords",
        "music ",
        "voice"
})

public class Trumpet {

    @JsonProperty("start")
    private Integer start;
    @JsonProperty("end")
    private Integer end;
    @JsonProperty("text")
    private String text;
    @JsonProperty("relevance")
    private Double relevance;
    @JsonProperty("keywords")
    private List<Keyword> keywords = null;
    @JsonProperty("music ")
    private List<Music> music = null;
    @JsonProperty("voice")
    private List<Voice> voice = null;
    @JsonIgnore
    private Map<String, Object> additionalProperties = new HashMap<String, Object>();

    @JsonProperty("start")
    public Integer getStart() {
        return start;
    }

    @JsonProperty("start")
    public void setStart(Integer start) {
        this.start = start;
    }

    @JsonProperty("end")
    public Integer getEnd() {
        return end;
    }

    @JsonProperty("end")
    public void setEnd(Integer end) {
        this.end = end;
    }

    @JsonProperty("text")
    public String getText() {
        return text;
    }

    @JsonProperty("text")
    public void setText(String text) {
        this.text = text;
    }

    @JsonProperty("relevance")
    public Double getRelevance() {
        return relevance;
    }

    @JsonProperty("relevance")
    public void setRelevance(Double relevance) {
        this.relevance = relevance;
    }

    @JsonProperty("keywords")
    public List<Keyword> getKeywords() {
        return keywords;
    }

    @JsonProperty("keywords")
    public void setKeywords(List<Keyword> keywords) {
        this.keywords = keywords;
    }

    @JsonProperty("music ")
    public List<Music> getMusic() {
        return music;
    }

    @JsonProperty("music ")
    public void setMusic(List<Music> music) {
        this.music = music;
    }

    @JsonProperty("voice")
    public List<Voice> getVoice() {
        return voice;
    }

    @JsonProperty("voice")
    public void setVoice(List<Voice> voice) {
        this.voice = voice;
    }

    @JsonAnyGetter
    public Map<String, Object> getAdditionalProperties() {
        return this.additionalProperties;
    }

    @JsonAnySetter
    public void setAdditionalProperty(String name, Object value) {
        this.additionalProperties.put(name, value);
    }

}
